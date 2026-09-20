# Provenance

- The original Mario Bros. 1 project was inspected earlier for reporting ideas. It has not been modified during this migration; its repository and task are separate.
- Active dependencies: gym-super-mario-bros 9.1.0, nes-py 9.0.1, Gymnasium 1.3.0, Stable Baselines3 2.9.0. Source inspection and real-game tests, rather than a package's name alone, establish the checks reported here.
- The installed `gym_super_mario_bros.smb3_env.SuperMarioBros3Env` provides task metadata and RAM observations. Our adapter subclasses it for the documented World 1-1 completion correction; it does not patch the installed package or another project.
