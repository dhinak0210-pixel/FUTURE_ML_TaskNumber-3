# Resume ML System

Production-grade ML system for automated resume screening and ranking.

## 🚀 Key Features

- **Advanced Resume Parsing**: Extract structured data from PDF, DOCX, and TXT files.
- **Semantic Skill Extraction**: Identify technical and soft skills using specialized NER models.
- **Deep Matcher**: Rank candidates against job descriptions using BERT-based embeddings.
- **Explainable AI**: Understand why a candidate was ranked highly with SHAP explanations.
- **Production-Ready API**: Deploy the screening engine via FastAPI.
- **Interactive Dashboard**: Explore screening results with a built-in Streamlit app.

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/resume-ml-system
cd resume-ml-system

# Install dependencies using Poetry
poetry install
```

## 🛠️ Usage

### Running the Demo
```bash
streamlit run app.py
```

### Starting the API
```bash
uvicorn src.resume_ml.api.fastapi_app:app --reload
```

## 🏗️ Project Structure

- `src/resume_ml`: Core logic and package source.
- `models/`: Trained ML weights (managed by Git LFS).
- `data/`: Sample datasets and processing scripts.
- `docs/`: Comprehensive project documentation.
- `tests/`: Extensive test suite.

## 🤝 Contributing

See [CONTRIBUTING.md](docs/contributing.md) for details on how to get involved.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
