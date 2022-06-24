class Module:
    def __init__(self, title):
        self.title = title
        self.exprs: list[Expression] = []

    def __repr__(self):
        nl = "\n"
        new = f'{nl}\t'
        return f"<Module(" \
               f"title={self.title}, " \
               f"exprs=" \
               f"{f'{new}{new.join([repr(rexp) for rexp in self.exprs])}{nl}' if len(self.exprs) else '[]'}" \
               f")>"  # big

    def add(self, exp):
        self.exprs.append(exp)


class Expression:
    def __repr__(self):
        return "<Expression()>"


class AssignmentExpression(Expression):
    def __init__(self, name_of_var: str, set_var_to, *types):
        self.name_of_var = name_of_var
        self.set_var_to = set_var_to
        self.types = types

    def __repr__(self):
        return f"<AssignmentExpression(name={self.name_of_var}, type={self.types}, set_to={self.set_var_to})>"
