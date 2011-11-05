# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/expdlist
# catalog-date 2008-06-23 23:47:50 +0200
# catalog-license lppl
# catalog-version 2.4
Name:		texlive-expdlist
Version:	2.4
Release:	1
Summary:	Expanded description environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/expdlist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expdlist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expdlist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expdlist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides additional features for the LaTeX
description environment, including adjustable left margin. The
package also allows the user to 'break' a list (for example, to
interpose a comment) without affecting the structure of the
list (so that, for example, numbered lists remain in sequence).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
