add_executable(picow_display
    pico_display.c
    hw_config.c
    )

target_link_libraries(picow_display
    FatFs_SPI

    pico_stdlib
    pico_multicore
    pico_sd_card
    
    hardware_gpio
    hardware_sync
    hardware_spi
    hardware_dma
    )

pico_add_extra_outputs(picow_display code)
