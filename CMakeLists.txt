###########################################
## COPY COMPILED LIBRARY INTO WRAPPER
###########################################
# This file is expected to be called from a higher-level
# CMakeLists.txt when compiling the C++ library.

# Where to place compiled library for Python wrapper
# TODO-TEMPLATE: Update this directory for your library namespace
set(PYTHON_LIB_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src/ITS/.../${LIB_NAME}/)

add_custom_target(
    COPY_LIB_TO_PYTHON ALL
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:${LIB_NAME}> ${PYTHON_LIB_DIR}
    DEPENDS ${LIB_NAME}
    COMMENT "Copying library to Python wrapper directory"
)
