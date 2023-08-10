#pragma once
#include <memory>
#include <unordered_map>
#include <mutex>
#include <shared_mutex>
#include "Python.h"
#include <object.h>
#include "yaml-cpp/yaml.h"
#include <yaml-cpp/node/node.h>


class YamlCacher
{
    struct YamlData;
public:
    static YamlCacher* get_singleton();

    PyObject *get_py_yaml_object(std::string a_absolute_path,
                                 std::vector<std::string> &a_keys);

    const std::unique_ptr<YamlData>& get_yaml(std::string a_absolute_path);

    YAML::Node get_yaml(std::string a_absolute_path,
                      std::vector<std::string>& a_keys);
private:
    struct YamlData
    {
        std::string cached_file_md5;
        std::shared_mutex lock;
        YAML::Node yaml;
    };

    std::unordered_map<std::string, std::unique_ptr<YamlData>> _yaml_cache_map;
    std::shared_mutex _yaml_cache_map_lock;


    PyObject *yaml_node_to_py_object(
        YAML::Node
            a_node) // this is expensive; caller when calling GET_YAML_PY()
                    // should be as specific with keys as possible
        ;
};