cmake_minimum_required (VERSION 2.6)
project (gemm C)

if ("${CMAKE_BUILD_TYPE}" STREQUAL "")
  set(CMAKE_BUILD_TYPE RELWITHDEBINFO)
endif()

if(EXISTS "${PROJECT_SOURCE_DIR}/cmake.arch.inc")
  include("${PROJECT_SOURCE_DIR}/cmake.arch.inc")
endif()
if (NOT BLAS_LIBRARIES)
find_package(BLAS REQUIRED)
endif()

set(BUILD_SHARED_LIBS 1)

add_library(gemm npdot.c)
set_target_properties(gemm PROPERTIES
  LIBRARY_OUTPUT_DIRECTORY ${PROJECT_SOURCE_DIR})
target_link_libraries(gemm ${BLAS_LIBRARIES})
