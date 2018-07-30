FROM ubuntu:18.04

# setting environment variable
ARG version="3.6.5"
ARG pyenvpath="/.pyenv"
ARG fver="1.0.2"
ARG name_of_venv="appflask"
ARG uWSGI_Ver="2.0.17"
ARG redis_Ver="2.10.6"

# pyenv PATH environment variable
ENV PYENV_ROOT ${pyenvpath}
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# network test tools
RUN apt update -y && apt install -y iputils-ping net-tools curl wget nmap

# pyenv
RUN apt install -y \
make build-essential libssl-dev zlib1g-dev libbz2-dev git \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils
RUN git clone git://github.com/yyuu/pyenv.git ${pyenvpath}
RUN pyenv install ${version}
RUN pyenv local ${version}

# flask and virtualenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ${pyenvpath}/plugins/pyenv-virtualenv
RUN pyenv virtualenv ${version} ${name_of_venv}
RUN pyenv local ${name_of_venv}
RUN pip install -U pip
RUN pip install Flask==${fver}

# uWSGI
RUN pip install uwsgi==${uWSGI_Ver}

# redis
RUN pip install redis==${redis_Ver}