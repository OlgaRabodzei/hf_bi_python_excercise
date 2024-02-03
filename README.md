# Installation

This project uses [poetry](https://python-poetry.org/) for dependency management.
You can install in by following the instructions in the official documentation 
or by running the following command, which will use pip to install it:

```bash
make install-base
```

Then to install application dependencies, run:
```bash
make install
```

If you want to run test and/or linting checks, you will also need the development dependencies, 
which could be installed with the following command:
```bash
make install-dev
```

# Usage

To run the application use the following command:
```bash
make run
```

The result files will be saved in the `results` directory.