#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	libmikey - C++ implementation of the MIKEY (RFC3830) protocol
Summary(pl):	libmikey - implementacja w C++ protoko�u MIKEY (RFC3830)
Name:		libmikey
Version:	0.4.0
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.minisip.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	8690f622409599e18a6325f5b9989f41
URL:		http://www.minisip.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libmutil-devel >= 0.3.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmikey implements the Multimedia Internet KEYing protocol, in a C++
library. The MIKEY protocol provides authentication and key agreement
for secure multimedia session.

%description -l pl
libmikey to biblioteka C++ implementuj�ca protok� Multimedia Internet
KEYing. Protok� ten zapewnia uwierzytelnianie i uzgadnianie kluczy
dla bezpiecznych sesji multimedialnych.

%package devel
Summary:	Header files for libmikey library
Summary(pl):	Pliki nag��wkowe biblioteki libmikey
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libmutil-devel >= 0.3.0

%description devel
Header files for libmikey library.

%description devel -l pl
Pliki nag��wkowe biblioteki libmikey.

%package static
Summary:	Static libmikey library
Summary(pl):	Statyczna biblioteka libmikey
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmikey library.

%description static -l pl
Statyczna biblioteka libmikey.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO
%attr(755,root,root) %{_libdir}/libmikey.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmikey.so
%{_libdir}/libmikey.la
%{_includedir}/libmikey

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmikey.a
%endif
