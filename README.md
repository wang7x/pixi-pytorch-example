# PyTorch Environment Demo Project

## Overview
This project demonstrates a properly configured PyTorch environment with GPU support using Pixi for dependency management. It includes verification tools to validate your PyTorch installation and GPU capabilities.

## Features
- ✅ Pre-configured PyTorch environment (CPU/GPU variants)
- ✅ CUDA 12.x compatibility
- ✅ Dependency management via Pixi
- ✅ Built-in installation verification script
- ✅ Hugging Face Hub integration

## Prerequisites
- Linux system (64-bit)
- NVIDIA GPU with CUDA 12.0+ drivers (for GPU support)
- [Pixi](https://pixi.sh/latest/install/) installed globally

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/pixi-pytroch-example.git
cd pixi-pytroch-example

# Install dependencies (GPU version by default)
pixi install
```

##Verification
Validate your PyTorch installation with:
```bash
pixi run check-pytorch
```

Expected successful output (GPU version):
```text
✅ PyTorch imported successfully

=== System Information ===
PyTorch version: 2.7.1
CUDA available: Yes

=== CUDA Information ===
CUDA version: 12.6
Current device: 0
Device name: NVIDIA GeForce RTX 4090
Device count: 1
Device memory: 24.00 GB

=== Tensor Operations Test ===
CPU addition successful | Shape: torch.Size([2, 3])
GPU addition successful | Device: cuda:0
✅ Basic operations validated

=== Verification Result ===
🎉 PyTorch installed correctly (GPU support enabled)
```

## Environment Management
Switch between environments:
```bash
# Use CPU-only environment
pixi activate cpu

# Use GPU environment (default)
pixi activate gpu
```

## Key Dependencies
| Package | Version |
|---------|---------|
| Python | 3.12 |
| PyTorch | ≥2.7.1, <3 |
| torchvision | ≥0.22.0, <0.23 |
| torchaudio | ≥2.7.1, <3 |
| huggingface-hub | ≥0.34.1, <0.35 |

## Troubleshooting
If GPU isn't detected:
1. Verify NVIDIA drivers are installed (`nvidia-smi`)
2. Ensure CUDA 12.x is properly configured
3. Check for version compatibility between:
   - NVIDIA drivers
   - System CUDA version
   - PyTorch CUDA version

For CPU-only installations:
```bash
pixi activate cpu
pixi run check-pytorch
```

## License
MIT License - see [LICENSE](LICENSE) file for details
