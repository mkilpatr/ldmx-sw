message(STATUS "Installing field map files ...")
execute_process(COMMAND git submodule init WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/../..)
execute_process(COMMAND git submodule update WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/../..)
file(MAKE_DIRECTORY ${CMAKE_INSTALL_PREFIX}/data/fieldmap)
file(GLOB fieldmap_files ${CMAKE_CURRENT_LIST_DIR}/../../MagFieldMap/*.tar.gz)
foreach(fieldmap_file ${fieldmap_files})
  execute_process(COMMAND tar -C ${CMAKE_INSTALL_PREFIX}/data/fieldmap -zxvf ${fieldmap_file})
endforeach()
message(STATUS "Done installing field map files.")