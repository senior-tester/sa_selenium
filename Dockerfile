FROM python
COPY ./test_main.py .
RUN pip install --upgrade pip
RUN pip install selenium pytest
CMD ["pytest", "test_main.py"]