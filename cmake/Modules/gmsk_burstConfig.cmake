INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_GMSK_BURST gmsk_burst)

FIND_PATH(
    GMSK_BURST_INCLUDE_DIRS
    NAMES gmsk_burst/api.h
    HINTS $ENV{GMSK_BURST_DIR}/include
        ${PC_GMSK_BURST_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GMSK_BURST_LIBRARIES
    NAMES gnuradio-gmsk_burst
    HINTS $ENV{GMSK_BURST_DIR}/lib
        ${PC_GMSK_BURST_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GMSK_BURST DEFAULT_MSG GMSK_BURST_LIBRARIES GMSK_BURST_INCLUDE_DIRS)
MARK_AS_ADVANCED(GMSK_BURST_LIBRARIES GMSK_BURST_INCLUDE_DIRS)

