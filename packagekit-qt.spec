%define api 4
%define major 0
%define binname packagekitqt
%define libname %mklibname %{binname} %{api} %{major}
%define devname %mklibname -d %{name}

Summary:	A DBUS packaging abstraction layer
Name:		packagekit-qt
Version:	0.9.5
Release:	2
License:	GPLv2+
Group:		System/Configuration/Packaging
Url:		http://www.packagekit.org
Source0:	http://www.freedesktop.org/software/PackageKit/releases/PackageKit-Qt-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	packagekit >= %{version}
BuildRequires:	pkgconfig(QtCore)
Requires:	packagekit >= %{version}

%description
PackageKit is a DBUS abstraction layer that allows the session user to manage
packages in a secure way using a cross-distro, cross-architecture API.

%package -n	%{libname}
Summary:	Libraries for accessing PackageKit-Qt
Group:		System/Configuration/Packaging
Requires:	packagekit >= %{version}

%description -n	%{libname}
Libraries for accessing PackageKit-Qt.

%package -n	%{devname}
Summary:	Libraries and headers for PackageKit
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	packagekit-devel < %{version}

%description -n %{devname}
Headers and libraries for PackageKit.

%prep
%setup -qn PackageKit-Qt-%{version}
%apply_patches

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/lib%{binname}%{api}.so.%{major}
%{_libdir}/lib%{binname}%{api}.so.%{version}

%files -n %{devname}
%{_includedir}/%{binname}%{api}/PackageKit
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/%{binname}%{api}

