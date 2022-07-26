//  Copyright (c) 2022 Intel Corporation
//
//  Licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.

#ifndef ENGINE_SPARSELIB_INCLUDE_KERNELS_LAYERNORM_BA_HPP_
#define ENGINE_SPARSELIB_INCLUDE_KERNELS_LAYERNO_BA_HPP_
#include "operator_desc.hpp"
#include "kernel.hpp"
#include "kernel_desc.hpp"
#include <vector>
#include "utils.hpp"
#include "layernorm_ba_types.hpp"
#include "jit_domain/jit_layernorm_ba.hpp"
namespace jd {
class layernorm_ba_k_t;

class layernorm_ba_kd_t : public kernel_desc_t {
 public:
  explicit layernorm_ba_kd_t(const jd::operator_desc& op_desc)
      : kernel_desc_t(kernel_kind::layernorm_ba), op_desc_(op_desc){};

  virtual ~layernorm_ba_kd_t() {
    delete one_;
    delete[] one_div_n_;
    delete[] eps_;
  }

 public:
  bool init() override;
  DECLARE_COMMON_PD_T(layernorm_ba_k_t, layernorm_ba_kd_t);

 public:
  const jd::operator_desc& operator_desc() const override { return op_desc_; }
  const std::vector<ssd::layernorm_ba_param_t>& params() const { return params_; }
  const float* one_div_n_ptr() const { return one_div_n_; }
  const float* eps_ptr() const { return eps_; }
  const float* one_ptr() const { return one_; }

 private:
  jd::operator_desc op_desc_;
  std::vector<ssd::layernorm_ba_param_t> params_;
  float* one_div_n_;
  float* one_;
  float* eps_;
};

class layernorm_ba_k_t : public kernel_t {
 public:
  using kd_t = layernorm_ba_kd_t;
  explicit layernorm_ba_k_t(const std::shared_ptr<const kd_t>& kd) : kernel_t(kd) {}
  virtual ~layernorm_ba_k_t() {}

 public:
  bool init() override;

  bool execute(const std::vector<const void*>& rt_data) const override;

 public:
  const std::shared_ptr<const kd_t> derived_kd() const { return std::static_pointer_cast<const kd_t>(kd_); }

 private:
  std::vector<jit_layernorm_ba_t*> jit_kers_;
  int64_t nthr_;
  std::vector<ssd::layernorm_ba_data_t*> td;
};

}  // namespace jd
#endif