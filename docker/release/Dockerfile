FROM paliwalanurag/flask-base:latest
MAINTAINER Anurag Paliwal <anuragpaliwal@live.in>

# Copy application artifacts
COPY target /wheelhouse

COPY docker/release/flask_settings.py /appenv

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse flaskuserapp && \
    rm -rf /wheelhouse
