#include <stdio.h>
#include <stdbool.h>
#include "pico/stdlib.h"
#include "hardware/spi.h"
#include "pico/stdio/driver.h"
#include "hardware/sync.h"
#include "hardware/gpio.h"
#include "pico/binary_info.h"
#include "pico/multicore.h"
#include "pico/stdlib.h"
#include "pico/stdio/driver.h"


// Display parameters
#define WIDTH 16
#define HEIGHT 16
#define NUM_DISPLAYS 6
#define BYTES_PER_DISPLAY 24

// SPI parameters
const uint SPI_PORT = 0;
const uint SPI_SCK_PIN = 18; // SCK Pin
const uint SPI_MOSI_PIN = 19; // MOSI Pin
const uint SPI_CS_PIN = 17; // CS Pin

// Variables setup
// Buffer to store incoming data
uint8_t data_buffer[WIDTH * HEIGHT * NUM_DISPLAYS * BYTES_PER_DISPLAY];

// Output pins setup   
const uint LED_PINS[NUM_DISPLAYS] = {0,1,2,3,4,5};


// SPI setup
void init_spi() {
    spi_inst_t *spi = spi0;
    spi_init(spi, 1000000); // TODO: Set SPI frequency
    gpio_set_function(SPI_SCK_PIN, GPIO_FUNC_SPI);
    gpio_set_function(SPI_MOSI_PIN, GPIO_FUNC_SPI);
}

// SD card initialization
bool init_sd_card() {
    stdio_set_translate_crlf(&stdio_uart, false);

    gpio_init(SPI_CS_PIN);
    gpio_set_dir(SPI_CS_PIN, GPIO_OUT);
    stdio_init_all();

    if (!sd_card_detect()) {
        printf("SD Card not detected\n");
        return false;
    }

    sleep_ms(10);

    if (!sd_card_init()) {
        printf("Failed to initialize SD Card\n");
        return false;
    }

    return true;
}

// Read pixel data from SD card
bool read_pixel_data(uint8_t *data_buffer, const char *filename) {
    FILE *file = fopen(filename, "rb");
    if (!file) {
        printf("Error opening file\n");
        return false;
    }

    size_t bytes_read = fread(data_buffer, 1, sizeof(data_buffer), file);
    fclose(file);

    if (bytes_read != sizeof(data_buffer)) {
        printf("Error reading file\n");
        return false;
    }

    return true;
}

int main() {
    stdio_init_all();

    // Initialize SPI
    init_spi();

    // Initialize SD Card
    if (!init_sd_card()) {
        return 1;
    }

    // Read pixel data from SD Card
    if (!read_pixel_data(data_buffer, "test.bin")) {
        return 1;
    }

    while (true) {

    }
}
