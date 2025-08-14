
#!/usr/bin/env python3
"""
Script to regenerate the OpenAPI client from the Pingera API specification.
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Generate the OpenAPI client."""
    
    print("Regenerating Pingera OpenAPI client...")
    
    # Paths
    spec_file = "attached_assets/openapi.json"
    output_dir = "client"
    
    # Check if spec file exists
    if not Path(spec_file).exists():
        print(f"Error: OpenAPI spec file not found: {spec_file}")
        sys.exit(1)
    
    # Remove existing client directory
    if Path(output_dir).exists():
        print("Removing existing client directory...")
        subprocess.run(["rm", "-rf", output_dir], check=True)
    
    # Generate command
    cmd = [
        "openapi-generator-cli", "generate",
        "-i", spec_file,
        "-g", "python",
        "-o", output_dir,
        "--package-name", "pingera",
        "--additional-properties", "packageVersion=1.0.2,projectName=pingera-generated-client"
    ]
    
    try:
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ Client generated successfully!")
        
        # Fix the license issue in the generated pyproject.toml
        pyproject_path = Path(output_dir) / "pyproject.toml"
        if pyproject_path.exists():
            print("Fixing license field in pyproject.toml...")
            with open(pyproject_path, 'r') as f:
                content = f.read()
            
            # Replace the invalid license format
            content = content.replace('license = "NoLicense"', 'license = {text = "MIT"}')
            
            with open(pyproject_path, 'w') as f:
                f.write(content)
            print("✓ License field fixed")
        
        # Install the generated client
        print("Installing generated client...")
        install_cmd = [sys.executable, "-m", "pip", "install", "-e", output_dir]
        subprocess.run(install_cmd, check=True)
        print("✓ Generated client installed!")
        
        print(f"\nGenerated client is available in: {output_dir}/")
        print("The client package name is: pingera_generated")
        print("You can now import and use: from pingera_generated import ApiClient, Configuration")
        
    except subprocess.CalledProcessError as e:
        print(f"Error generating client: {e}")
        if e.stdout:
            print(f"STDOUT: {e.stdout}")
        if e.stderr:
            print(f"STDERR: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: openapi-generator command not found.")
        print("Please install it with: pip install openapi-generator-cli[jdk4py]")
        sys.exit(1)


if __name__ == "__main__":
    main()
