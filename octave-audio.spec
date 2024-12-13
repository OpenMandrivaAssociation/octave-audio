%global octpkg audio
%global optflags %{optflags} -I%{_includedir}/rtmidi

Summary:	Audio and MIDI Toolbox for GNU Octave
Name:		octave-audio
Version:	2.0.9
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/audio/
Source0:	https://github.com/gnu-octave/octave-audio/releases/download/release-%{version}/audio-%{version}.tar.gz

BuildRequires:	octave-devel >= 4.0.0
BuildRequires:	pkgconfig(rtmidi)
BuildRequires:	texinfo

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
The Audio toolkit is a set of functions for manipulating MIDI devices and
files for GNU Octave.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

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

