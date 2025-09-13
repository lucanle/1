add_library(quant_core STATIC
    order_book.cpp
    matching_engine.cpp
    event_loop.cpp
)

target_include_directories(quant_core PUBLIC 
    ${CMAKE_CURRENT_SOURCE_DIR}/../../include
)

target_compile_options(quant_core PRIVATE -O3 -march=native)