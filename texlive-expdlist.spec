Name:		texlive-expdlist
Version:	15878
Release:	2
Summary:	Expanded description environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/expdlist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expdlist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expdlist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expdlist.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides additional features for the LaTeX
description environment, including adjustable left margin. The
package also allows the user to 'break' a list (for example, to
interpose a comment) without affecting the structure of the
list (so that, for example, numbered lists remain in sequence).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/expdlist/expdlist.sty
%doc %{_texmfdistdir}/doc/latex/expdlist/expdlisg.pdf
%doc %{_texmfdistdir}/doc/latex/expdlist/expdlist.pdf
%doc %{_texmfdistdir}/doc/latex/expdlist/readme.txt
#- source
%doc %{_texmfdistdir}/source/latex/expdlist/expdlisg.drv
%doc %{_texmfdistdir}/source/latex/expdlist/expdlist.drv
%doc %{_texmfdistdir}/source/latex/expdlist/expdlist.dtx
%doc %{_texmfdistdir}/source/latex/expdlist/expdlist.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
