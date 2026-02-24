#!/bin/bash
set -e

echo "🚀 Setting up Resume ML development environment..."

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -
export PATH="/home/vscode/.local/bin:$PATH"

# Configure Poetry
poetry config virtualenvs.in-project true

# Install dependencies
echo "📦 Installing dependencies..."
poetry install --with dev,notebook

# Install pre-commit hooks
echo "🔧 Installing pre-commit hooks..."
poetry run pre-commit install

# Download spaCy models
echo "🧠 Downloading NLP models..."
poetry run python -m spacy download en_core_web_trf

# Pull Git LFS files
echo "📥 Pulling large files..."
git lfs pull

# Create .env file if not exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
fi

echo "✅ Setup complete! Run 'poetry shell' to activate environment."
