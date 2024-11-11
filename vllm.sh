export CUDA_VISIBLE_DEVICES=0,1,2,3
nohup vllm serve "meta-llama/Llama-3.1-8B-Instruct" --pipeline-parallel-size 4 > vllm.log 2>&1 &