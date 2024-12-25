cmake_minimum_required(VERSION 3.25.1)
project(test VERSION 0.0.1 LANGUAGES CXX)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Include directories
include_directories(include)

# Source files
set(SOURCES
    src/main.cpp
    src/hello/hello.cpp
)

# Add the executable
add_executable(${PROJECT_NAME} ${SOURCES})
