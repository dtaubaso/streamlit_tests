import streamlit as st


st.title("Probar videos")

with st.expander("Ver argumentos"):
    st.write("""Parameters
        ----------
        data : str, Path, bytes, io.BytesIO, numpy.ndarray, or file
            The video to play. This can be one of the following:

            - A URL (string) for a hosted video file, including YouTube URLs.
            - A path to a local video file. The path can be a ``str``
              or ``Path`` object. Paths can be absolute or relative to the
              working directory (where you execute ``streamlit run``).
            - Raw video data. Raw data formats must include all necessary file
              headers to match the file format specified via ``format``.

        format : str
            The MIME type for the video file. This defaults to ``"video/mp4"``.
            For more information, see https://tools.ietf.org/html/rfc4281.

        start_time: int, float, timedelta, str, or None
            The time from which the element should start playing. This can be
            one of the following:

            - ``None`` (default): The element plays from the beginning.
            - An ``int`` or ``float`` specifying the time in seconds. ``float``
              values are rounded down to whole seconds.
            - A string specifying the time in a format supported by `Pandas'
              Timedelta constructor <https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html>`_,
              e.g. ``"2 minute"``, ``"20s"``, or ``"1m14s"``.
            - A ``timedelta`` object from `Python's built-in datetime library
              <https://docs.python.org/3/library/datetime.html#timedelta-objects>`_,
              e.g. ``timedelta(seconds=70)``.
        subtitles: str, bytes, Path, io.BytesIO, or dict
            Optional subtitle data for the video, supporting several input types:

            - ``None`` (default): No subtitles.

            - A string, bytes, or Path: File path to a subtitle file in
              ``.vtt`` or ``.srt`` formats, or the raw content of subtitles
              conforming to these formats. Paths can be absolute or relative to
              the working directory (where you execute ``streamlit run``).
              If providing raw content, the string must adhere to the WebVTT or
              SRT format specifications.

            - io.BytesIO: A BytesIO stream that contains valid ``.vtt`` or ``.srt``
              formatted subtitle data.

            - A dictionary: Pairs of labels and file paths or raw subtitle content in
              ``.vtt`` or ``.srt`` formats to enable multiple subtitle tracks.
              The label will be shown in the video player. Example:
              ``{"English": "path/to/english.vtt", "French": "path/to/french.srt"}``

            When provided, subtitles are displayed by default. For multiple
            tracks, the first one is displayed by default. If you don't want any
            subtitles displayed by default, use an empty string for the value
            in a dictrionary's first pair: ``{"None": "", "English": "path/to/english.vtt"}``

            Not supported for YouTube videos.
        end_time: int, float, timedelta, str, or None
            The time at which the element should stop playing. This can be
            one of the following:

            - ``None`` (default): The element plays through to the end.
            - An ``int`` or ``float`` specifying the time in seconds. ``float``
              values are rounded down to whole seconds.
            - A string specifying the time in a format supported by `Pandas'
              Timedelta constructor <https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html>`_,
              e.g. ``"2 minute"``, ``"20s"``, or ``"1m14s"``.
            - A ``timedelta`` object from `Python's built-in datetime library
              <https://docs.python.org/3/library/datetime.html#timedelta-objects>`_,
              e.g. ``timedelta(seconds=70)``.
        loop: bool
            Whether the video should loop playback.
        autoplay: bool
            Whether the video should start playing automatically. This is
            ``False`` by default. Browsers will not autoplay unmuted videos
            if the user has not interacted with the page by clicking somewhere.
            To enable autoplay without user interaction, you must also set
            ``muted=True``.
        muted: bool
            Whether the video should play with the audio silenced. This is
            ``False`` by default. Use this in conjunction with ``autoplay=True``
            to enable autoplay without user interaction.
""")

video_url = st.text_input("Ingrese la url del video")

if st.button("Ver video"):
    if video_url:
        try:
            st.video(video_url)
        except Exception as e:
            st.error(f"Ocurrio un error {e}")
    else:
        st.error("No hay url de video")