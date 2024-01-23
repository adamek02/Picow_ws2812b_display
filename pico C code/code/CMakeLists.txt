add_executable(${PROJECT}
        ${PROJECT}.c
        )

target_include_directories(${PROJECT} PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}
        ${CMAKE_CURRENT_LIST_DIR}/.. # for our common lwipopts
        )
target_link_libraries(${PROJECT}
        pico_cyw43_arch_none
        pico_stdlib
        )
pico_add_extra_outputs(${PROJECT})
