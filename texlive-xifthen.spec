%global tl_name xifthen
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4.0
Release:	%{tl_revision}.1
Summary:	Extended conditional commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xifthen
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xifthen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xifthen.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package extends the ifthen package by implementing new commands to
go within the first argument of \ifthenelse: to test whether a string is
void or not, if a command is defined or equivalent to another. The
package also enables use of complex expressions as introduced by the
package calc, together with the ability of defining new commands to
handle complex tests.

