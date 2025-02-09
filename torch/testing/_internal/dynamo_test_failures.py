# We generate unittest.expectedFailure for all of the following tests
# when run under PYTORCH_TEST_WITH_DYNAMO=1.
#
# This lists exists so we can more easily add large numbers of failing tests,
dynamo_expected_failures = {
    "TestCppExtensionJIT.test_cpp_frontend_module_has_up_to_date_attribute",
    "TestCppExtensionJIT.test_custom_compound_op_autograd",
    "TestCppExtensionJIT.test_cpp_frontend_module_has_up_to_date_attributes",
    "TestCppExtensionOpenRgistration.test_open_device_registration",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch1d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch1d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch1d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNN.test_Conv2d_missing_argument",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch1d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch1d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch1d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch1d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch1d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch2d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel2d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch2d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel2d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch2d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel2d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel2d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch2d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel3d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch2d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel3d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch2d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel3d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel3d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch2d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel3d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel3d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch2d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel3d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch3d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel3d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch3d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel1d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel1d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch3d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel1d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch3d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel1d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel1d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch3d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel1d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch3d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel1d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch3d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel1d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch3d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel2d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel2d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel1d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel2d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel1d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel2d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel1d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel2d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel1d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel2d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel1d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel1d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel2d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel2d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel1d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel1d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel3d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel3d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel2d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel2d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel3d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel2d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_batch_channel2d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel3d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel3d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel3d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel3d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_empty_channel3d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel2d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel2d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel2d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel1d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel3d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel1d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel1d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel3d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel3d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel1d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel3d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel3d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel1d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel3d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel3d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel1d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel3d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel3d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel1d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel3d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel1d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel3d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel2d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel2d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel1d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel2d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel1d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel2d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel1d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel1d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_batch_channel2d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel1d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel1d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel1d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel1d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel2d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel2d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel2d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel2d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel2d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel2d_has_bias_True_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel2d_has_bias_True_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel2d_has_bias_True_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel3d_has_bias_False_strided_False_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel3d_has_bias_False_strided_False_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel3d_has_bias_False_strided_True_contiguous_False_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel3d_has_bias_False_strided_True_contiguous_True_cpu",
    "TestConvolutionNNDeviceTypeCPU.test_conv_backend_mkldnn_empty_channel3d_has_bias_True_strided_False_contiguous_False_cpu",
    "TestPoolingNN.test_MaxUnpool2d_output_size",
    "TestIndexingCPU.test_zero_dim_index_cpu",
    "NumpyTestsCPU.test_boolean_indexing_weirdness_cpu",
    "FakeTensorConverterTest.test_memoized_conversion_from_meta",
    "NumpyTestsCPU.test_boolean_shape_mismatch_cpu",
    "FakeTensorOperatorInvariants.test_like_ops",
    "FakeTensorOperatorInvariants.test_non_kwarg_only_device",
    "FakeTensorOperatorInvariants.test_tensor_constructors_all_have_kwarg_device",
    "NumpyTestsCPU.test_empty_fancy_index_cpu",
    "NumpyTestsCPU.test_index_no_floats_cpu",
    "TestLinalgCPU.test_addmm_sizes_cpu_float32",
    "TestLinalgCPU.test_addmm_sizes_cpu_float64",
    "TestLinalgCPU.test_addr_integral_cpu_int16",
    "TestLinalgCPU.test_addr_integral_cpu_int32",
    "TestLinalgCPU.test_addr_integral_cpu_int64",
    "TestLinalgCPU.test_addr_integral_cpu_int8",
    "TestLinalgCPU.test_addr_integral_cpu_uint8",
    "TestIndexingCPU.test_empty_ndim_index_bool_cpu",
    "TestPythonDispatcher.test_quantized_structured_not_implemented",
    "TestIndexingCPU.test_index_cpu",
    "TestIndexingCPU.test_invalid_index_cpu",
    "TestIndexingCPU.test_out_of_bound_index_cpu",
    "TestLinalgCPU.test_inverse_cpu_complex128",
    "TestLinalgCPU.test_inverse_cpu_complex64",
    "TestLinalgCPU.test_inverse_cpu_float32",
    "TestLinalgCPU.test_inverse_cpu_float64",
    "TestLinalgCPU.test_matmul_small_brute_force_3d_Nd_cpu_complex64",
    "TestLinalgCPU.test_matmul_small_brute_force_3d_Nd_cpu_float32",
    "TestLinalgCPU.test_matmul_small_brute_force_3d_Nd_cpu_int64",
    "TestLinalgCPU.test_linalg_lu_family_cpu_complex128",
    "TestLinalgCPU.test_linalg_lu_family_cpu_complex64",
    "TestLinalgCPU.test_linalg_lu_family_cpu_float32",
    "TestLinalgCPU.test_linalg_lu_family_cpu_float64",
    "TestLinalgCPU.test_einsum_random_cpu_complex128",
    "TestLinalgCPU.test_einsum_random_cpu_float64",
    "TestLinalgCPU.test_einsum_sublist_format_cpu_complex128",
    "TestLinalgCPU.test_einsum_sublist_format_cpu_float64",
    "TestLinalgCPU.test_geqrf_cpu_complex128",
    "TestLinalgCPU.test_geqrf_cpu_complex64",
    "TestLinalgCPU.test_norm_dtype_cpu_float64",
    "TestLinalgCPU.test_geqrf_cpu_float32",
    "TestLinalgCPU.test_geqrf_cpu_float64",
    "TestLinalgCPU.test_householder_product_cpu_complex128",
    "TestLinalgCPU.test_householder_product_cpu_complex64",
    "TestLinalgCPU.test_householder_product_cpu_float32",
    "TestLinalgCPU.test_householder_product_cpu_float64",
    "TestLinalgCPU.test_norm_vector_cpu_float32",
    "TestLinalgCPU.test_norm_vector_cpu_float64",
    "TestLinalgCPU.test_norm_bfloat16_and_half_cpu_bfloat16",
    "TestLinalgCPU.test_norm_bfloat16_and_half_cpu_float16",
    "TestLinalgCPU.test_norm_dtype_cpu_complex128",
    "TestLinalgCPU.test_pinv_cpu_float64",
    "TestLinalgCPU.test_slogdet_errors_and_warnings_cpu_complex128",
    "TestLinalgCPU.test_slogdet_errors_and_warnings_cpu_complex64",
    "TestLinalgCPU.test_slogdet_errors_and_warnings_cpu_float32",
    "TestLinalgCPU.test_slogdet_errors_and_warnings_cpu_float64",
    "TestLinalgCPU.test_solve_cpu_complex128",
    "TestLinalgCPU.test_solve_cpu_complex64",
    "TestLinalgCPU.test_solve_cpu_float32",
    "TestLinalgCPU.test_solve_cpu_float64",
    "TestLinalgCPU.test_lobpcg_torchscript_cpu_float64",
    "TestLinalgCPU.test_pinv_cpu_complex128",
    "TestLinalgCPU.test_pinv_cpu_complex64",
    "TestLinalgCPU.test_pinv_cpu_float32",
}
