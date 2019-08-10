cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()


include(cotire) # This should work if everything is set up right

add_executable(example example.cpp example2.cpp)

cotire(example)

# cotire sets the following properties
get_target_property(_unitySource example COTIRE_CXX_UNITY_SOURCE)
get_target_property(_prefixHeader example COTIRE_CXX_PREFIX_HEADER)
get_target_property(_precompiledHeader example COTIRE_CXX_PRECOMPILED_HEADER)
get_target_property(_unityTargetName example COTIRE_UNITY_TARGET_NAME)

if (_unitySource)
	message(STATUS "example unity source: ${_unitySource}")
endif()
if (_prefixHeader)
	message(STATUS "example prefix header: ${_prefixHeader}")
endif()
if (_precompiledHeader)
	message(STATUS "example precompiled header: ${_precompiledHeader}")
endif()
if (TARGET ${_unityTargetName})
	message(STATUS "example unity target: ${_unityTargetName}")
endif()