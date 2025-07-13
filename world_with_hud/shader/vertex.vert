// Vertex Shader
#version 410 core
uniform int u_mode_v;
uniform vec3 u_m_pos;
uniform vec3 u_m_size;
uniform vec3 u_m_rot;
uniform vec3 u_c_pos;
uniform vec3 u_c_rot;
uniform vec4 u_c_proj;
in vec4 a_position;
in vec2 a_texcoord;
out vec2 p_texcoord;

void main() {
    if (u_move_v == 0) {
        gl_Position = a_position;
    } else {
        gl_Position = a_position;
    }
    p_texcoord = a_texcoord
}