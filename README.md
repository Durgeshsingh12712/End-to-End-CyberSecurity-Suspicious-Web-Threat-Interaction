# End-to-End-CyberSecurity-Suspicious-Web-Threat-Interaction

# Cybersecurity Threat Detection System

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-latest-green.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-red.svg)

An end-to-end machine learning project for detecting suspicious network activities and potential cybersecurity threats using advanced ML algorithms and real-time prediction capabilities.

## 🚀 Features

- **🔍 Data Ingestion**: Automated data collection and preprocessing pipeline
- **✅ Data Validation**: Comprehensive schema validation and data quality checks
- **🔄 Data Transformation**: Advanced feature engineering and data preprocessing
- **🤖 Model Training**: Ensemble approach with Random Forest and Neural Network models
- **📊 Model Evaluation**: Comprehensive performance metrics and model comparison
- **🌐 Web Interface**: Interactive Flask-based web application for real-time predictions
- **📝 Logging**: Comprehensive logging system for monitoring and debugging
- **⚠️ Exception Handling**: Robust custom exception handling throughout the pipeline
- **🔧 Modular Design**: Clean, modular architecture following software engineering best practices

## 🏗️ Project Architecture

```
cybersecurity_threat_detection/
├── cyberSecurity/
│       │
│       ├── components/          # Core ML pipeline components
│       │   ├── data_ingestion.py
│       │   ├── data_validation.py
│       │   ├── data_transformation.py
│       │   ├── model_trainer.py
│       │   └── model_evaluation.py
│       ├── configure/              # Configuration management
│       │   └── configuration.py
│       ├── entity/              # Data classes and entities
│       │   ├── config_entity.py
│       │   └── artifact_entity.py
│       ├── pipeline/            # Training and prediction pipelines
│       │   ├── training_pipeline.py
│       │   └── prediction_pipeline.py
│       ├── utils/               # Utility functions
│       │   ├── common.py
│       │   └── tools.py
│       ├── constants/           # Project constants
│       │    └──constant.py 
│       ├──loggers/              # Logging configuration
│       │  └──logger.py
│       ├──exception/            # Custom exception handling
│          └──exception.py         
├── config/                      # Configuration files
│   ├── config.yaml
│   └── params.yaml
├── artifacts/                   # Generated artifacts and models
├── logs/                        # Application logs
├── templates/                   # HTML templates for web interface
│   ├── index.html
│   └── results.html
├── app.py                       # Flask web application
├── main.py                      # Training pipeline runner
├── requirements.txt             # Project dependencies
├── setup.py                     # Package setup
└── README.md                    # Project documentation
```

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <https://github.com/Durgeshsingh12712/End-to-End-CyberSecurity-Suspicious-Web-Threat-Interaction.git>
cd End-to-End-CyberSecurity-Suspicious-Web-Threat-Interaction
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv cyber_env

# Activate virtual environment
# On Windows:
cyber_env\Scripts\activate
# On macOS/Linux:
source cyber_env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Package in Development Mode
```bash
pip install -e .
```

## 🚦 Getting Started

### Training the Model

1. **Run the complete training pipeline:**
```bash
python main.py
```

This will execute the following stages:
- Data ingestion and preprocessing
- Data validation and quality checks
- Feature engineering and transformation
- Model training (Random Forest + Neural Network)
- Model evaluation and selection

### Starting the Web Application

1. **Launch the Flask web server:**
```bash
python app.py
```

2. **Access the application:**
Open your browser and navigate to `http://localhost:5000`

## 🎯 Usage

### Web Interface

1. **Input Parameters**: Enter network traffic parameters including:
   - Bytes In: Amount of incoming data
   - Bytes Out: Amount of outgoing data
   - Duration: Connection duration in seconds
   - Source IP Country Code: Origin country of the traffic

2. **Get Results**: Click "Analyze Threat" to get real-time threat assessment

3. **Interpret Results**: 
   - ✅ **Normal Activity**: Traffic appears legitimate
   - ⚠️ **Suspicious Activity**: Potential security threat detected

### Programmatic Usage

```python
from cyberSecurity.pipeline.prediction_pipeline import PredictPipeline, CustomData

# Create prediction pipeline
predict_pipeline = PredictPipeline()

# Create custom data instance
data = CustomData(
    bytes_in=1500.0,
    bytes_out=800.0,
    duration_seconds=120.5,
    src_ip_country_code="US"
)

# Get prediction
df = data.get_data_as_data_frame()
result = predict_pipeline.predict(df)
print("Threat Status:", "Suspicious" if result[0] == 1 else "Normal")
```

## 🤖 Model Details

### Algorithms Used

1. **Random Forest Classifier**
   - n_estimators: 100
   - max_depth: 10
   - random_state: 42

2. **Neural Network (TensorFlow/Keras)**
   - Architecture: Dense layers [128, 64, 32, 1]
   - Activation: ReLU (hidden), Sigmoid (output)
   - Optimizer: Adam (lr=0.001)
   - Regularization: Dropout (0.3)

### Features

The model analyzes the following features:
- **bytes_in**: Incoming data volume
- **bytes_out**: Outgoing data volume  
- **duration_seconds**: Connection duration
- **src_ip_country_code**: Geographic origin

### Performance Metrics

The system evaluates models using:
- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score

## 📁 Configuration

### config/config.yaml
Contains paths and configuration for each pipeline stage:
```yaml
artifacts_root: artifacts
data_ingestion:
  root_dir: artifacts/data_ingestion
  source_URL: <https://raw.githubusercontent.com/Durgeshsingh12712/Data-All/refs/heads/main/Unified%20Dataset/CloudWatch_Traffic_Web_Attack.csv>
  # ... other configurations
```

### config/params.yaml
Contains hyperparameters for models and preprocessing:
```yaml
RANDOM_FOREST:
  n_estimators: 100
  max_depth: 10
  # ... other parameters
```

## 📊 Monitoring and Logging

- **Logs Location**: `logs/` directory
- **Log Format**: Timestamped with component name and log level
- **Exception Tracking**: Detailed error messages with file and line information

## 🔧 Development

### Adding New Features

1. Create new components in `cyberSecurity/components/`
2. Update configuration entities in `cyberSecurity/entity/`
3. Modify pipelines in `cyberSecurity/pipeline/`
4. Update configuration files in `config/`

### Testing

```bash
# Run individual components
python -c "from cyberSecurity.components.data_ingestion import DataIngestion; print('Component test')"
```

## 🚨 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure package is installed in development mode
2. **Path Issues**: Check that all paths in config files are correct
3. **Memory Issues**: Reduce batch size in neural network configuration
4. **Data Issues**: Verify data format matches expected schema

### Debug Mode

Enable debug logging by modifying `cyberSecurity/loggers/logger.py`:
```python
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Model Performance

Expected performance metrics:
- **Accuracy**: 85-95%
- **Precision**: 80-90%
- **Recall**: 85-92%
- **F1-Score**: 82-91%

*Note: Actual performance depends on data quality and hyperparameter tuning.*

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add comprehensive docstrings
- Include unit tests for new components
- Update documentation for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Scikit-learn community for machine learning tools
- TensorFlow team for deep learning framework
- Flask community for web framework
- Contributors and maintainers

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the logs in the `logs/` directory

---

**⚡ Quick Start Commands:**
```bash
# Complete setup and run
git clone <https://github.com/Durgeshsingh12712/End-to-End-CyberSecurity-Suspicious-Web-Threat-Interaction.git>
cd End-to-End-CyberSecurity-Suspicious-Web-Threat-Interaction
python -m venv cyber_env
source cyber_env/bin/activate  # or cyber_env\Scripts\activate on Windows
pip install -r requirements.txt
pip install -e .
python main.py
python app.py
```

**🌐 Access the application at: http://localhost:5000**