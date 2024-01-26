#include <stdio.h>
#include <stdbool.h>
#include "pico/stdlib.h"
#include "hardware/spi.h"
#include "pico/stdio/driver.h"
#include "hardware/gpio.h"
#include "pico/binary_info.h"
#include "pico/multicore.h"
#include "sd_card.h"
#include "ff.h"

// Display parameters
#define WIDTH 16
#define HEIGHT 16
#define NUM_DISPLAYS 6
#define BYTES_PER_DISPLAY 24
#define BYTES_PER_FRAME (WIDTH * HEIGHT * BYTES_PER_DISPLAY)

// SPI parameters
const uint SPI_PORT = 0;
const uint SPI_SCK_PIN = 2;  // SCK Pin
const uint SPI_MOSI_PIN = 3; // MOSI Pin
const uint SPI_MISO_PIN = 4; // MISO Pin
const uint SPI_CS_PIN = 5;   // CS Pin


// Buffer to store incoming data for one frame
uint8_t frame_buffer[BYTES_PER_FRAME];

// Output pins setup
const uint LED_PINS[NUM_DISPLAYS] = {21, 20, 19, 18, 17, 16};

// SD Card file parameters
const char *filename = "example.bin";
FIL file;

//SPI setup
void init_spi() {
    spi_inst_t *spi = spi0;
    spi_init(spi, 12500000); // 12.5 MHz
    gpio_set_function(SPI_SCK_PIN, GPIO_FUNC_SPI);
    gpio_set_function(SPI_MOSI_PIN, GPIO_FUNC_SPI);
}

// PIO setup
#define PIO_DISPLAY_PROGRAM_SIZE 32
static uint32_t pio_display_program[PIO_DISPLAY_PROGRAM_SIZE];

void init_pio_display_program() {
    // PIO program to separate the inputted bitstream into six buffers for WS2812B displays
    // Assumes the bitstream is organized in rows of 16 pixels, and you provide data for a whole 16x16 block

    // PIO program: separate bitstream into six buffers for WS2812B displays
    // Adjust the constants based on your specific requirements

    // Constants for buffer sizes and display layout
    const int pixels_per_row = 16;
    const int bits_per_pixel = 1;  // Assuming you provide 1 bit for each pixel (WS2812B data format)
    const int pixels_per_display = 256;  // Total pixels per display
    const int displays_per_row = 3;      // Displays per row (1 3 5, 2 4 6)

    // Number of rows per display
    const int rows_per_display = pixels_per_display / pixels_per_row;

    for (int display = 0; display < displays_per_row; display++) {
        for (int row = 0; row < rows_per_display; row++) {
            for (int pixel = 0; pixel < pixels_per_row; pixel++) {
                // Calculate the bit offset in the frame_buffer
                int bit_offset = (display * pixels_per_display + row * pixels_per_row + pixel) * bits_per_pixel;

                // Calculate the word and bit offsets in the PIO program
                int word_offset = display * rows_per_display + row;
                int bit_in_word = pixel * bits_per_pixel;

                // Load the corresponding bits from the frame_buffer to the PIO program
                pio_display_program[word_offset] |= pio_encode_mov(false, LED_PINS[display], bits_per_pixel);
            }
        }
    }
}

// Function to execute the display on the second core
void core1_display() {
    // Initialize PIO program for display
    init_pio_display_program();

    // PIO setup
    // Example: This assumes the existence of a hypothetical configure_pio function
    // Modify this function according to your PIO configuration
    // configure_pio(pio, sm, SPI_SCK_PIN, SPI_MOSI_PIN, SPI_CS_PIN);

    while (1) {
        // Implement your display logic here
        // Example: You may need to load data from the frame buffer and send it to adjacent displays
        // This example assumes the existence of a hypothetical display_function function
        // Modify this function according to your display logic
        // display_function(frame_buffer, LED_PINS);
    }
}

int main() {
    stdio_init_all();

    // Initialize SPI
    init_spi();

    // Initialize SD Card
    if (!sd_init_driver()) {
        return 20;
    }

    // Open the binary file
    if (f_open(&file, filename, FA_READ) != FR_OK) {
        printf("Error opening file: %s\n", filename);
        return 1;
    }

    // Start the second core for display
    multicore_launch_core1(core1_display);

    while (1) {
        // Read data for one frame from the file
        UINT bytesRead;
        if (f_read(&file, frame_buffer, BYTES_PER_FRAME, &bytesRead) != FR_OK) {
            printf("Error reading file: %s\n", filename);
            break;
        }

        // Check for end of file
        if (bytesRead == 0) {
            break;
        }

        // Wait for the second core to finish processing the previous frame
        multicore_fifo_pop_blocking();

        // Send the frame data to the second core
        multicore_fifo_push_blocking((uint32_t)frame_buffer);

        // Your main program logic goes here
    }

    // Close the file
    f_close(&file);

    return 0;
}
