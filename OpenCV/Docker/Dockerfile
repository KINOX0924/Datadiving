# 1. 베이스 이미지 선택 (NVIDIA의 공식 텐서플로우 이미지를 기반으로 시작)
# 이 안에는 CUDA, cuDNN, TensorFlow, Python이 모두 포함되어 있습니다.
FROM nvcr.io/nvidia/tensorflow:24.06-tf2-py3

# 2. 시스템 환경 변수 설정
# apt-get 설치 과정에서 불필요한 대화형 프롬프트를 방지합니다.
ENV DEBIAN_FRONTEND=noninteractive

# 3. 리눅스 시스템 라이브러리 설치 (가장 중요)
# apt-get은 리눅스의 프로그램 설치 관리자입니다.
# 이 과정이 없으면 OpenCV가 동영상이나 다양한 이미지 파일을 처리할 때 에러가 발생합니다.
RUN apt-get update && apt-get install -y --no-install-recommends \
    # FFmpeg: 동영상 코덱을 위한 필수 라이브러리 (비디오 처리용)
    ffmpeg \
    # 이미지 처리에 필요한 그래픽 라이브러리들
    libgl1-mesa-glx \
    libglib2.0-0 \
    # OpenCV가 의존하는 X11 관련 라이브러리들
    libsm6 \
    libxext6 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 4. pip를 이용해 파이썬 라이브러리들을 영구적으로 설치
# --no-cache-dir 옵션은 불필요한 캐시를 남기지 않아 이미지 용량을 줄여줍니다.
# 3. pip를 이용해 필요한 파이썬 라이브러리들을 영구적으로 설치
RUN pip install --no-cache-dir \
    "numpy<2.0" \
    opencv-python-headless \
    matplotlib \
    seaborn \
    scikit-learn \
    scikit-image \
    pandas \
    jupyterlab

# 5. 컨테이너의 기본 작업 환경 설정
# 컨테이너에 접속했을 때 기본으로 위치할 폴더입니다.
WORKDIR /workspace

# 6. 컨테이너의 포트 개방
# 컨테이너의 8888 포트를 외부(내 PC)에 노출시킵니다. (JupyterLab 접속용)
EXPOSE 8888

# 7. 컨테이너가 시작될 때 자동으로 실행할 기본 명령어
# 여기서는 JupyterLab을 외부에서 접속 가능하도록 실행합니다.
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]