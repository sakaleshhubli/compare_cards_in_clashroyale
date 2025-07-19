# Clash Royale Card Explorer

## About

A Flask web application that fetches Clash Royale card data from the official API and lets users compare 2-8 cards side by side.

## Features

- Real-time card data from Clash Royale API
- Compare key stats: elixir cost, rarity, type, and descriptions
- Simple checkbox selection interface
- Lightweight and fast

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo.git
   cd your-repo
   ```

2. Set up Python environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install flask
   ```

3. Add your API key:
   - Create `mykey.txt` in the root directory
   - Paste your Clash Royale API token (no whitespace)

4. Run the app:
   ```bash
   python app.py
   ```
   Access at: `http://127.0.0.1:5000/`

## Usage

1. Open the app in your browser
2. Select 2-8 cards using checkboxes
3. Click "Compare Selected Cards" to view:
   - Card images
   - Elixir costs
   - Rarities
   - Types
   - Descriptions

## How It Works

- Fetches card data from Clash Royale API on startup
- Stores data in memory for quick access
- Uses Flask templates for the web interface
- Simple checkbox-based selection system

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request
