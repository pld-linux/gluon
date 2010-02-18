
%define		qtver	4.6.2
%define		snap	201002181913 # YYYYMMddHHmm
%define		kdever	4.4.0

Summary:	Gluon
Summary(pl.UTF-8):	Gluon
Name:		gluon
Version:	0
Release:	0.%{snap}.1
License:	GPL v2
Group:		X11/Libraries
# git clone git://gitorious.org/gluon/gluon.git
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	68fe1589e77ed0a134e1d026607dc8c9
URL:		http://gluon.tuxfamily.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtDesigner-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtUiTools-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.84
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gluon is a cross-platform free and open source 2D game engine from
KDE. It aims to make life easier for game developers by providing a
simple but powerful API to handle 2D objects, sounds and inputs.

#%description -l pl.UTF-8

%prep
%setup -q -n %{name}-%{snap}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
