%define		file_version	%(echo %{version} | tr . -)
Summary:	Sega Master System Emulator
Summary(pl.UTF-8):	Emulator Sega Master System
Name:		osmose
Version:	0.9.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://bcz.emu-france.com/osmose/Osmose-%{file_version}-src.zip
# Source0-md5:	fafa52a39e6fe194b34fa2cfd0df7466
Patch0:		%{name}-Makefile.patch
URL:		http://bcz.emu-france.com/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	unzip
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Osmose is an Object oriented sega master system designed for first for
Linux.

%description -l pl.UTF-8
Osmose jest obiektowo zorientowanym systemem sega master stworzonym
przede wszystkim dla Linuksa.

%prep
%setup -q -n Osmose-%{file_version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install osmose $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changes.txt readme.txt
%attr(755,root,root) %{_bindir}/osmose
