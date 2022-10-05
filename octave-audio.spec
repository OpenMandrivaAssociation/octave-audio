%global octpkg audio

Summary:	Audio recording, processing and playing tools
Name:		octave-%{octpkg}
Version:	2.0.5
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel > 4.0.0
BuildRequires:	pkgconfig(rtmidi)
BuildRequires:	texinfo

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The Audio toolkit is a set of functions for manipulating MIDI devices and
files for GNU Octave.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -n %{octpkg}-%{version}

%build
export LIBS="-L%{_libdir}"
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

