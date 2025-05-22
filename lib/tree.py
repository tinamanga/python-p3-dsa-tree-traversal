class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id_to_find):
        return self._dfs(self.root, id_to_find)

  def _dfs(self, node, id_to_find):
        if node['id'] == id_to_find:
            return node
        for child in node.get('children', []):
            result = self._dfs(child, id_to_find)
            if result:
                return result
        return None