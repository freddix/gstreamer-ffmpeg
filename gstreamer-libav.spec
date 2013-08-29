%include	/usr/lib/rpm/macros.gstreamer

%define		gstname		gst-libav
%define		gst_major_ver	1.0

Summary:	GStreamer Streaming-media framework plug-in using FFmpeg
Name:		gstreamer-libav
Version:	1.0.10
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://gstreamer.freedesktop.org/src/gst-libav/%{gstname}-%{version}.tar.xz
# Source0-md5:	715564cdb735dad75b0e770e044488e0
URL:		http://gstreamer.net/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	libav-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	rpm-gstreamerprov
Requires:	gstreamer-plugins-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer is a streaming-media framework, based on graphs of filters
which operate on media data. Applications using this library can do
anything from real-time sound processing to playing videos, and just
about anything else media-related. Its plugin-based architecture means
that new data types or processing capabilities can be added simply by
installing new plug-ins.

This plugin contains the FFmpeg codecs, containing codecs for most
popular multimedia formats.

%prep
%setup -qn %{gstname}-%{version}

sed -i -e '/sleep 15/d' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--with-libav-extra-configure="--enable-runtime-cpudetect"
#	--with-system-libav
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-%{gst_major_ver}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstavscale.so
%attr(755,root,root) %{_libdir}/gstreamer-%{gst_major_ver}/libgstlibav.so

