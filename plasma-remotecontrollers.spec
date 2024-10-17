%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Remote control interface for Plasma, primarily for use with plasma-bigscreen
Name:		plasma-remotecontrollers
Version:	5.27.11
Release:	2
License:	LGPL
Group:		System/Libraries
Url:		https://plasma-bigscreen.org/
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Package)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(QtWaylandScanner)
BuildRequires:	cmake(WaylandScanner)
BuildRequires:	cmake(KScreenLocker) < 5.27.50
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	cmake(LibTaskManager) < 5.27.50
BuildRequires:	cmake(PlasmaWaylandProtocols) >= 1.4.0
BuildRequires:	pkgconfig(Qt5WaylandClient)
BuildRequires:	pkgconfig(libcec)
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	qml(org.kde.plasma.core)
Requires:	qml(org.kde.plasma.core)

%description
Remote control interface for Plasma, primarily for use with plasma-bigscreen.

%files -f %{name}.lang
%{_sysconfdir}/xdg/autostart/org.kde.plasma-remotecontrollers.desktop
%{_sysconfdir}/xdg/plasma-remotecontrollersrc
%{_bindir}/plasma-remotecontrollers
%{_libdir}/qt5/plugins/kcms/kcm_mediacenter_remotecontrollers.so
%{_libdir}/qt5/qml/org/kde/plasma/remotecontrollers
%{_libdir}/udev/rules.d/40-uinput.rules
%{_datadir}/applications/org.kde.plasma-remotecontrollers.desktop
%{_datadir}/knotifications5/plasma-remotecontrollers.notifyrc
%{_datadir}/kpackage/kcms/kcm_mediacenter_remotecontrollers
%{_datadir}/kservices5/kcm_mediacenter_remotecontrollers.desktop
%{_datadir}/metainfo/org.kde.plasma.remotecontrollers.metainfo.xml
%{_datadir}/qlogging-categories5/plasma-remotecontrollers.categories
%{_datadir}/dbus-1/interfaces/org.kde.plasma.remotecontrollers.CEC.xml
%{_datadir}/dbus-1/interfaces/org.kde.plasma.remotecontrollers.ControllerManager.xml
%{_datadir}/dbus-1/interfaces/org.kde.plasma.remotecontrollers.EVDEV.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name
