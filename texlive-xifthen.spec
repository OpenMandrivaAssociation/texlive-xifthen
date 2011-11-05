# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xifthen
# catalog-date 2009-05-03 12:26:51 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-xifthen
Version:	1.3
Release:	1
Summary:	Extended conditional commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xifthen
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xifthen.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xifthen.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package extends the ifthen package by implementing new
commands to go within the first argument of \ifthenelse: to
test whether a string is void or not, if a command is defined
or equivalent to another. The package also enables use of
complex expressions as introduced by the package calc, together
with the ability of defining new commands to handle complex
tests. The package requires e-TeX features.

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
%{_texmfdistdir}/tex/latex/xifthen/xifthen.sty
%doc %{_texmfdistdir}/doc/latex/xifthen/README
%doc %{_texmfdistdir}/doc/latex/xifthen/xifthen.pdf
%doc %{_texmfdistdir}/doc/latex/xifthen/xifthen.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
