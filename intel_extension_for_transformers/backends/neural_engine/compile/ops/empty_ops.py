#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The neural engine empty op file."""

from .op import Operator, operator_registry
from .tensor import Tensor


# x + y element-wise, supports broadcasting
@operator_registry(operator_type='AddV2')
class AddV2(Operator):
    """Register the AddV2 operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='MultiHeadAttenion')
class MultiHeadAttenion(Operator):
    def __init__(self):
        super().__init__()

# x + y element-wise, supports broadcasting
@operator_registry(operator_type='Add')
class Add(Operator):
    """Register the Add operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='BinaryAdd')
class BinaryAdd(Operator):
    """Register the BinaryAdd operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='ConstantOfShape')
class ConstantOfShape(Operator):
    """Register the ConstantOfShape operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='DequantizeLinear')
class DequantizeLinear(Operator):
    """Register the DequantizeLinear operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Computes the Gauss error function of x element-wise.
@operator_registry(operator_type='Erf')
class Erf(Operator):
    """Register the Erf operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='Expand')
class Expand(Operator):
    """Register the Expand operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# This operation creates a tensor of shape dims and fills it with value.
# tf.fill(dims, value, name=None)
@operator_registry(operator_type='Fill')
class Fill(Operator):
    """Register the Fill operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='FlatMapDataset')
class FlatMapDataset(Operator):
    """Register the FlatMapDataset operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='Identity')
class Identity(Operator):
    """Register the Identity operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Fused_op MatMul + BiasAdd
# The inputs are two-dimensional matrices and 1-D const bias
@operator_registry(operator_type='InnerProduct')
@operator_registry(operator_type='InnerProductGraph')
class InnerProduct(Operator):
    """Register the InnerProduct operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# store input_tensors for engine
@operator_registry(operator_type='Input')
class Input(Operator):
    """Register the Input operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Fused_op Mean, AddV2, Mul, etc.
# This pattern has several ops combinations, so the input_tensors and output_tensors may various
@operator_registry(operator_type='LayerNorm')
class LayerNorm(Operator):
    """Register the LayerNorm operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='MakeIterator')
class MakeIterator(Operator):
    """Register the MakeIterator operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Fused_op MatMulWithBias + Add/AddV2
# The inputs are two-dimensional matrices, 1-D const bias and one tensor from Add op
@operator_registry(operator_type='MatMulWithBiasAdd')
class MatMulWithBiasAdd(Operator):
    """Register the MatMulWithBiasAdd operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Fused_op MatMulWithBias + Gelu
# The inputs are two-dimensional matrices and 1-D const bias
@operator_registry(operator_type='MatMulWithBiasGelu')
class MatMulWithBiasGelu(Operator):
    """Register the MatMulWithBiasGelu operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Fused_op MatMulWithBias + Tanh
# The inputs are two-dimensional matrices and 1-D const bias
@operator_registry(operator_type='MatMulWithBiasTanh')
class MatMulWithBiasTanh(Operator):
    """Register the MatMulWithBiasTanh operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Fused_op MatMul + BiasAdd
# The inputs are two-dimensional matrices and 1-D const bias
@operator_registry(operator_type='MatMulWithBias')
class MatMulWithBias(Operator):
    """Register the MatMulWithBias operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# store the output_tensors for engine
@operator_registry(operator_type='Output')
class Output(Operator):
    """Register the Output operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Fused_op Reshape, ExpandDims+Sub+Mul
# This pattern is used for dealing with input_mask originally in bert model
@operator_registry(operator_type='PaddingSequence')
class PaddingSequence(Operator):
    """Register the PaddingSequence operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Given a tensor x and a tensor y ,
# this operation computes x^y for corresponding elements in x and y
@operator_registry(operator_type='Pow')
class Pow(Operator):
    """Register the Pow operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='QLinearMatMul')
class QLinearMatMul(Operator):
    """Register the QLinearMatMul operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='QLinearAdd')
class QLinearAdd(Operator):
    """Register the QLinearAdd operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='QLinearMul')
class QLinearMul(Operator):
    """Register the QLinearMul operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Returns x / y element-wise for real types.
# If x and y are reals, this will return the floating-point division.
# RealDiv supports broadcasting
@operator_registry(operator_type='RealDiv')
class RealDiv(Operator):
    """Register the RealDiv operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# tf.math.rsqrt(x, name=None)
# Computes reciprocal of square root of x element-wise.
@operator_registry(operator_type='Rsqrt')
class Rsqrt(Operator):
    """Register the Rsqrt operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# tf.shape(input, out_type=tf.dtypes.int32, name=None)
# Returns a tensor containing the shape of the input tensor.
@operator_registry(operator_type='Shape')
class Shape(Operator):
    """Register the Shape operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Computes element-wise square root of the input tensor.
@operator_registry(operator_type='Sqrt')
class Sqrt(Operator):
    """Register the Sqrt operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Computes square of x element-wise.
@operator_registry(operator_type='Square')
class Square(Operator):
    """Register the Square operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# tf.math.squared_difference(x, y, name=None)
# Returns conj(x - y)(x - y) element-wise, supports broadcasting
@operator_registry(operator_type='SquaredDifference')
class SquaredDifference(Operator):
    """Register the SquaredDifference operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='StopGradient')
class StopGradient(Operator):
    """Register the StopGradient operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Given an input tensor, this function computes hyperbolic tangent of every element in the tensor.
@operator_registry(operator_type='Tanh')
class Tanh(Operator):
    """Register the Tanh operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='TensorSliceDataset')
class TensorSliceDataset(Operator):
    """Register the TensorSliceDataset operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


# Fused_op Reshape, Transpose and BatchMatMul / BatchMatMulV2
# This pattern has several ops combinations, so the input_tensors and output_tensors may various
@operator_registry(operator_type='TransposeBatchMatMul')
class TransposeBatchMatMul(Operator):
    """Register the TransposeBatchMatMul operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='Where')
class Where(Operator):
    """Register the Where operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='Range')
class Range(Operator):
    """Register the Range operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='Relu')
class Relu(Operator):
    """Register the Relu operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='MatMulWithBiasRelu')
class MatMulWithBiasRelu(Operator):
    """Register the MatMulWithBiasRelu operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='Matmul')
class Matmul(Operator):
    """Register the Matmul operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='Quantize')
class Quantize(Operator):
    """Register the Quantize operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()


@operator_registry(operator_type='CumSum')
class CumSum(Operator):
    """Register the CumSum operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='Onehot')
class Onehot(Operator):
    """Register the Onehot operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='TokenTypeIds')
class TokenTypeIds(Operator):
    """Register the TokenTypeIds operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='PositionIds')
class PositionIds(Operator):
    """Register the PositionIds operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='Loop')
class Loop(Operator):
    """Register the Loop operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='Sigmoid')
class Sigmoid(Operator):
    """Register the Sigmoid operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='MatMulWithBiasSigmoid')
class MatMulWithBiasSigmoid(Operator):
    """Register the MatMulWithBiasSigmoid operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='EmbeddingBag')
class EmbeddingBag(Operator):
    """Register the EmbeddingBag operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='Flatten')
class Flatten(Operator):
    """Register the Flatten operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='Reorder')
class Reorder(Operator):
    """Register the Reorder operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='MergedEmbeddingbag')
class MergedEmbeddingbag(Operator):
    """Register the MergedEmbeddingbag operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='Convolution')
class Convolution(Operator):
    """Register the Convolution operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='ExpandIndices')
class ExpandIndices(Operator):
    """Register the ExpandIndices operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='Tile')
class Tile(Operator):
    """Register the Tile operator."""
    def __init__(self):
        """The init function of this operator."""
        super().__init__()

@operator_registry(operator_type='OpAny')
class OpAny(Operator):
    """Register the OpAny operator."""
    def __init__(self):
        """The init function of this operator."""

@operator_registry(operator_type='SequenceLength')
class SequenceLength(Operator):

    def __init__(self):
        super().__init__()

