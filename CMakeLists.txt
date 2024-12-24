cmake_minimum_required(VERSION 3.25.1)
project(Test)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Include directories
include_directories(/home/vcoliver/Documents/Coding/CMake/include)

# Source files
set(SOURCES
    main.cpp
)

# Add the executable
add_executable(Test ${SOURCES})