name: Generate Font Showcase

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Debug information
      run: |
        pwd
        ls -R

    - name: Generate HTML
      run: |
        cd Fontbrowse
        python generate_showcase.py

    - name: Commit changes
      run: |
        git config --local user.email "shadowdragongtas@gmail.com"
        git config --local user.name "ssshingetsu"
        git add Fontbrowse/index.html
        git commit -m "Update font showcase" -a || echo "No changes to commit"
        git push
