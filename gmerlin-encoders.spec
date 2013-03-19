# TODO: subpackages for individual encoder plugins (by required libs)?
Summary:	Encoder plugins for gmerlin
Summary(pl.UTF-8):	Wtyczki kodujące dla gmerlina
Name:		gmerlin-encoders
Version:	1.2.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gmerlin/%{name}-%{version}.tar.gz
# Source0-md5:	db401732dde0c27702ad3303956cb158
Patch0:		%{name}-am.patch
Patch1:		%{name}-link.patch
URL:		http://gmerlin.sourceforge.net/avdec_frame.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	faac-devel >= 1.24
# avcodec build >= 3412992, libpostproc >= 51.0.0, libswscale >= 0.5.0
BuildRequires:	ffmpeg-devel >= 0.7
BuildRequires:	flac-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	gmerlin-devel >= 1.2.0
BuildRequires:	lame-libs-devel >= 3.93
BuildRequires:	libogg-devel >= 1:1.1
BuildRequires:	libshout-devel >= 2.2.2
BuildRequires:	libtheora-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	mjpegtools-devel >= 1.9.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	speex-devel >= 1.0.4
Requires:	faac >= 1.24
Requires:	ffmpeg-libs >= 0.7
Requires:	flac >= 1.2.0
Requires:	gmerlin >= 1.2.0
Requires:	lame-libs >= 3.93
Requires:	libogg >= 1:1.1
Requires:	libshout >= 2.2.2
Requires:	libtheora >= 1.0.0
Requires:	libvorbis >= 1:1.0
Requires:	mjpegtools >= 1.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer -ffast-math

%description
This package contains some encoder plugins for gmerlin. If you install
it, gmerlin-transcoder will be able to encode more file formats.

%description -l pl.UTF-8
Ten pakiet zawiera wtyczki kodujące dla gmerlina. Po zainstalowaniu
tego pakietu gmerlin-transcoder będzie w stanie kodować do większej
liczby formatów plików.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# evil, sets CFLAGS basing on /proc/cpuinfo, overrides our optflags
# (--with-cpuflags=none disables using /proc/cpuinfo, but not overriding)
sed -i -e '19,$d;18aAC_DEFUN([LQT_OPT_CFLAGS],[OPT_CFLAGS="$CFLAGS"])' m4/lqt_opt_cflags.m4

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gmerlin/plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/gmerlin/plugins/b_lame.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/b_ogg.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_faac.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_ffmpeg.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_ffmpeg_audio.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_ffmpeg_video.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_flac.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_flacogg.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_lame.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_mpeg.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_mpegaudio.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_mpegvideo.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_speex.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_theora.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_vorbis.so
%attr(755,root,root) %{_libdir}/gmerlin/plugins/e_yuv4mpeg.so
