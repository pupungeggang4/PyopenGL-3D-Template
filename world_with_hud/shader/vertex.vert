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
    if (u_mode_v == 0) {
        gl_Position = a_position;
    } else {
        mat4 m_m_pos = mat4(
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            u_m_pos.x, u_m_pos.y, u_m_pos.z, 1.0
        );
        mat4 m_m_size = mat4(
            u_m_size.x, 0.0, 0.0, 0.0,
            0.0, u_m_size.y, 0.0, 0.0,
            0.0, 0.0, u_m_size.z, 0.0,
            0.0, 0.0, 0.0, 1.0
        );
        mat4 m_c_pos = mat4(
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, 1.0, 0.0,
            u_c_pos.x, u_c_pos.y, u_c_pos.z, 1.0
        );
        mat4 m_z_inv = mat4(
            1.0, 0.0, 0.0, 0.0,
            0.0, 1.0, 0.0, 0.0,
            0.0, 0.0, -1.0, 0.0,
            0.0, 0.0, 0.0, 1.0
        );
        float fov = u_c_proj[0];
        float asp = u_c_proj[1];
        float near = u_c_proj[2];
        float far = u_c_proj[3];
        mat4 m_c_proj = mat4(
            1.0 / (asp * tan(fov / 2.0)), 0.0, 0.0, 0.0,
            0.0, tan(fov / 2.0), 0.0, 0.0,
            0.0, 0.0, -(far + near) / (far - near), -1.0,
            0.0, 0.0, -(2.0 * far * near) / (far - near), 0.0
        );
        vec4 pos = a_position;
        pos = m_m_pos * pos;
        pos = m_m_size * pos;
        pos = m_z_inv * pos;
        pos = m_c_pos * pos;
        pos = m_c_proj * pos;
        gl_Position = pos;
    }
    p_texcoord = a_texcoord;
}