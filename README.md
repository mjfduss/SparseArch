# SparseArch

## Baselines
Environments and command to run training:
- CartPole-v1
    - `python rl-baselines3-zoo/train.py --algo ppo_lstm --env CartPole-v1 --eval-episodes 10 --eval-freq 10000 --track --wandb-project-name thesis --conf-file benchmark_configs/benchmark_baseline_custom.yml`
- Acrobot-v1
    - `python rl-baselines3-zoo/train.py --algo ppo_lstm --env Acrobot-v1 --eval-episodes 10 --eval-freq 10000 --track --wandb-project-name thesis`
- BipedalWalker-v3
    - `python rl-baselines3-zoo/train.py --algo ppo_lstm --env BipedalWalker-v3 --eval-episodes 10 --eval-freq 10000 --track --wandb-project-name thesis`
- LunarLander-v2
    - `python rl-baselines3-zoo/train.py --algo ppo_lstm --env LunarLander-v2 --eval-episodes 10 --eval-freq 10000 --track --wandb-project-name thesis --conf-file benchmark_configs/benchmark_baseline_custom.yml`