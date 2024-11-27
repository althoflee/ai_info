# streamlit laucher setup

```json
"configurations": [
        {
            "name": "Streamlit : Current File",
            "type": "debugpy",
            "request": "launch",
            "module" : "streamlit",
            "console": "integratedTerminal",
            "justMyCode": true,
            "cwd" : "${fileDirname}",
            "args": [
                "run",
                "${file}",
                "--server.port",
                "8501",
                "--",
                "--debugger",
                "--verbose"
            ]
        }
    ]
    ```