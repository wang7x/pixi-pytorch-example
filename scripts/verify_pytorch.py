"""
PyTorch Installation Verification Script
Purpose: Validate PyTorch installation and GPU support
"""

try:
    import torch
    print("✅ PyTorch imported successfully")
except ImportError:
    print("❌ PyTorch not installed properly")
    exit(1)

# ===== System Information =====
print("\n=== System Information ===")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {'Yes' if torch.cuda.is_available() else 'No'}")

# ===== CUDA Information =====
if torch.cuda.is_available():
    print("\n=== CUDA Information ===")
    print(f"CUDA version: {torch.version.cuda}")
    print(f"Current device: {torch.cuda.current_device()}")
    print(f"Device name: {torch.cuda.get_device_name(0)}")
    print(f"Device count: {torch.cuda.device_count()}")
    print(f"Device memory: {torch.cuda.get_device_properties(0).total_memory/1e9:.2f} GB")
else:
    print("\n⚠️  CUDA unavailable. Potential reasons:")
    print("- NVIDIA drivers not installed")
    print("- PyTorch installed without GPU support")
    print("- CUDA/PyTorch version mismatch")

# ===== Tensor Operations Test =====
print("\n=== Tensor Operations Test ===")
try:
    # CPU test
    a = torch.randn(2, 3)
    b = torch.randn(2, 3)
    c = a + b
    print(f"CPU addition successful | Shape: {c.shape}")

    # GPU test (if available)
    if torch.cuda.is_available():
        device = torch.device("cuda:0")
        a_gpu = a.to(device)
        b_gpu = b.to(device)
        c_gpu = a_gpu + b_gpu
        print(f"GPU addition successful | Device: {c_gpu.device}")

    print("✅ Basic operations validated")
except Exception as e:
    print(f"❌ Operation test failed: {str(e)}")

# ===== Final Verification Result =====
print("\n=== Verification Result ===")
if torch.cuda.is_available():
    print("🎉 PyTorch installed correctly (GPU support enabled)")
else:
    print("⚠️  PyTorch installed but no GPU support detected")
