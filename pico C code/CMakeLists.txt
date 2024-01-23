cmake_minimum_required(VERSION 3.13)

set(PROJECT picow_display)
set(PICO_BOARD pico_w)

# Pull in SDK (must be before project)
include(pico_sdk_import.cmake)

include(pico_extras_import_optional.cmake)

project(${PROJECT} C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

if (PICO_CYW43_SUPPORTED) # set by PICO_BOARD=pico_w

endif()


# Initialize the SDK
pico_sdk_init()


    # enable usb output, disable uart output
  #  pico_enable_stdio_usb(${PROJECT} 1)
   # pico_enable_stdio_uart(${PROJECT} 0)

    add_subdirectory(code)

