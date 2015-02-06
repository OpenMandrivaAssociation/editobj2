%define	oname	EditObj2

Name: 	 	editobj2
Summary: 	Tkinter dialog box for editing any Python object

Version: 	0.4
Release: 	2
Source:		EditObj2-%{version}.tar.gz
URL:		http://home.gna.org/oomadness/en/editobj/
License:	GPLv2
Group:		Development/Python
BuildRequires:  python-devel
Requires:	tkinter
Obsoletes:	editobj
BuildArch:	noarch

%description
EditObj2 can create and display a Tkinter dialog box for editing any Python
object (similarly to what Java call a Bean editor, but for Python object).
EditObj2 is a useful tool for writing (text or non-text) editors of all
kinds, including GUI editor, 3D editor,... It also includes a Python console.

EditObj2 supports also lists, dictionaries and hierarchies (nested lists)
edition. EditObj2 includes also a tree widget for Tkinter, an event framework
and a mutiple undo/redo system.

%prep
%setup -q -n %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%clean

%files
%doc AUTHORS LICENSE README 
%{py_puresitedir}/%{name}
%{py_puresitedir}/*.egg-info


