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

# Possible improvements

- Convert string literals to constants or configuration files
- Provide a way to configure the app through input parameters. E.g. input file URL, output directory, etc.
- Add input validation
- Add logging
- If different types of sources and destinations are expected, consider using a factory pattern to create the appropriate reader and writer.
- If input files are expected to be extremely large, consider using Dask or Spark to process them in parallel.