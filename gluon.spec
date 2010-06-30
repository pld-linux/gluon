
%define		qtver	4.6.3
# YYYYMMddHHmm
%define		snap	201002181913
%define		kdever	4.4.5

Summary:	Gluon
Summary(pl.UTF-8):	Gluon
Name:		gluon
Version:	0.70.0
Release:	1
License:	GPL v2
Group:		X11/Libraries
# git clone git://gitorious.org/gluon/gluon.git
# Source0:	%{name}-%{snap}.tar.gz
Source0:	http://gluon.gamingfreedom.org/sites/default/files/%{name}-%{version}.tar.gz
# Source0-md5:	3f5b6eae22a5c4f41e574b5ef5c66a8e
URL:		http://gluon.tuxfamily.org/
BuildRequires:	OpenAL-devel >= 1.8.466
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
BuildRequires:	eigen >= 2.0.12
BuildRequires:	glew-devel
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	libsndfile-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gluon is a cross-platform free and open source 2D game engine from
KDE. It aims to make life easier for game developers by providing a
simple but powerful API to handle 2D objects, sounds and inputs.

#%description -l pl.UTF-8

%package devel
Summary:	Header files for gluon
Summary(pl.UTF-8):	Pliki nagłówkowe dla gluona
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gluon.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla gluona.

%prep
%setup -q -n %{name}-%{name}

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
%attr(755,root,root) %{_bindir}/gluoncreator
%attr(755,root,root) %{_bindir}/gluonplayer
%dir %{_libdir}/gluon
%attr(755,root,root) %{_libdir}/gluon/libgluon_asset_script.so
%attr(755,root,root) %{_libdir}/gluon/libgluon_asset_sound.so
%attr(755,root,root) %{_libdir}/gluon/libgluon_asset_texture.so
%attr(755,root,root) %{_libdir}/gluon/libgluon_component_cameracontroller.so
%attr(755,root,root) %{_libdir}/gluon/libgluon_component_qtscript.so
%attr(755,root,root) %{_libdir}/gluon/libgluon_component_soundemitter.so
%attr(755,root,root) %{_libdir}/gluon/libgluon_component_soundlistener.so
%attr(755,root,root) %{_libdir}/gluon/libgluon_component_spriterenderer.so
%attr(755,root,root) %{_libdir}/gluon/libgluon_component_keyboardinput.so
%attr(755,root,root) %{_libdir}/gluon/libgluon_component_spherecollision.so
%attr(755,root,root) %{_libdir}/gluon/libgluon_component_textrenderer.so
%attr(755,root,root) %{_libdir}/kde4/gluon_creator_dockplugin_componentsdock.so
%attr(755,root,root) %{_libdir}/kde4/gluon_creator_dockplugin_messagedock.so
%attr(755,root,root) %{_libdir}/kde4/gluon_creator_dockplugin_projectdock.so
%attr(755,root,root) %{_libdir}/kde4/gluon_creator_dockplugin_propertiesdock.so
%attr(755,root,root) %{_libdir}/kde4/gluon_creator_dockplugin_scenedock.so
%attr(755,root,root) %{_libdir}/kde4/gluon_creator_dockplugin_viewwidgetdock.so
%attr(755,root,root) %{_libdir}/libGluonAudio.so.0.70.0
%attr(755,root,root) %{_libdir}/libGluonCore.so.0.70.0
%attr(755,root,root) %{_libdir}/libGluonCreator.so.0.70.0
%attr(755,root,root) %{_libdir}/libGluonEngine.so.0.70.0
%attr(755,root,root) %{_libdir}/libGluonGraphics.so.0.70.0
%attr(755,root,root) %{_libdir}/libGluonInput.so.0.70.0
%{_desktopdir}/kde4/gluon-creator.desktop
%{_datadir}/apps/gluoncreator
%{_datadir}/config.kcfg/gluoncreatorsettings.kcfg
%{_datadir}/kde4/services/gluon_creator_dockplugin_componentsdock.desktop
%{_datadir}/kde4/services/gluon_creator_dockplugin_messagedock.desktop
%{_datadir}/kde4/services/gluon_creator_dockplugin_projectdock.desktop
%{_datadir}/kde4/services/gluon_creator_dockplugin_propertiesdock.desktop
%{_datadir}/kde4/services/gluon_creator_dockplugin_scenedock.desktop
%{_datadir}/kde4/services/gluon_creator_dockplugin_viewwidgetdock.desktop
%{_datadir}/kde4/servicetypes/gluoncreator_plugin.desktop
%{_iconsdir}/hicolor/*x*/apps/gluon_creator.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGluonAudio.so
%attr(755,root,root) %{_libdir}/libGluonCore.so
%attr(755,root,root) %{_libdir}/libGluonCreator.so
%attr(755,root,root) %{_libdir}/libGluonEngine.so
%attr(755,root,root) %{_libdir}/libGluonGraphics.so
%attr(755,root,root) %{_libdir}/libGluonInput.so
%{_datadir}/cmake/Modules/FindGluon.cmake
%{_datadir}/cmake/Modules/FindGluonAudio.cmake
%{_datadir}/cmake/Modules/FindGluonCore.cmake
%{_datadir}/cmake/Modules/FindGluonCreator.cmake
%{_datadir}/cmake/Modules/FindGluonEngine.cmake
%{_datadir}/cmake/Modules/FindGluonGraphics.cmake
%{_datadir}/cmake/Modules/FindGluonInput.cmake
%dir %{_datadir}/gluon
%dir %{_datadir}/gluon/cmake
%{_datadir}/gluon/cmake/FindGLEW.cmake
%{_datadir}/gluon/cmake/FindGluon.cmake
%{_datadir}/gluon/cmake/FindGluonAudio.cmake
%{_datadir}/gluon/cmake/FindGluonCore.cmake
%{_datadir}/gluon/cmake/FindGluonCreator.cmake
%{_datadir}/gluon/cmake/FindGluonEngine.cmake
%{_datadir}/gluon/cmake/FindGluonGraphics.cmake
%{_datadir}/gluon/cmake/FindGluonInput.cmake
%{_datadir}/gluon/cmake/FindOggVorbis.cmake
%{_datadir}/gluon/cmake/FindSndFile.cmake
%{_includedir}/gluon
